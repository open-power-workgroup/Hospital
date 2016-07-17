require 'json'
require 'haml'
require 'sequel'
require 'sqlite3'

DB = Sequel.sqlite("./hospital.db")

json_content = File.read("./china-province-city-district-list/area.json")
json_obj = JSON.parse(json_content)

@provinces = json_obj["l"]
@provinces_array = {}

f=File.open("./draft2/html/index.html","w")
template = Tilt.new('index.haml')
f.puts template.render(self)
f.close


@provinces.each do |province|
	template = Tilt.new('province.haml')
	@province_name=province["n"]
	@hospitals = DB["select * from hospitals where province='#{province["s"]}' order by city"].all
	@putians = {}
	DB["select hospital_id,count(*) as cnt from evidences where type='putian' group by hospital_id"].each do |row|
		@putians[row[:hospital_id]] = row[:cnt]
	end

	f=File.open("./draft2/html/#{province["e"]}.html","w")
	f.puts template.render(self)
	f.close
	@provinces_array[province["s"]] = province["e"]
end

DB["select * from hospitals"].all.each do |hospital|
	template = Tilt.new('hospital.haml')
	locations = DB["select * from locations where hospital_id=?", hospital[:id]].all
	sites = DB["select * from sites where hospital_id=?", hospital[:id]].all
	evidences = DB["select * from evidences where hospital_id=? order by type", hospital[:id]].all

	f=File.open("./draft2/html/#{hospital[:id]}.html","w")
	f.puts template.render(self,:hospital=>hospital,:locations=>locations,:sites=>sites,:evidences=>evidences)
	f.close
end