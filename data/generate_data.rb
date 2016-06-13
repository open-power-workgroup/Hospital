require 'sequel'
require 'sqlite3'
require 'yaml'
require 'json'
require 'pp'

DB = Sequel.sqlite("./hospital.db")

class Location < Sequel::Model
end

class Site < Sequel::Model
end

class Evidence < Sequel::Model
end

class Hospital < Sequel::Model
  one_to_one :location
  one_to_many :sites
  one_to_many :baidu_evidences, :class=>:Evidence, :type=>'baidu'
  one_to_many :putian_evidences, :class=>:Evidence, :type=>'putian'
  one_to_many :news_list, :class=>:Evidence, :type=>'news'
  one_to_many :comment_list, :class=>:Evidence, :type=>'comment'
end

with_baidu_json_data = JSON.parse(File.read("./baidu_hospital_with_trust.json"))
with_baidu_json_data.each do |json_data|
  hospital = Hospital.where(:bdv=>json_data["bdv"]).first || Hospital.new
  hospital.bdv = json_data["bdv"]
  hospital.name = json_data["name"]
  hospital.type = json_data["type"]
  hospital.desc = json_data["desc"]
  hospital.save
  puts "#{hospital.name} saved."
  json_data["sites"].each do |site_data|
    site = Site.where(:url=>site_data["url"],:hospital_id=>hospital.id).first || Site.new
    site.name = site_data["name"]
    site.domain = site_data["domain"]
    site.url = site_data["url"]
    site.auth = site_data["auth"]
    site.icp = site_data["icp"]
    site.org = site_data["org"]
    site.hospital_id = hospital.id
    site.save
    puts "#{site.url} saved."
  end
end

without_baidu_json_data = JSON.parse(File.read("./baidu_hospital_without_trust.json"))
without_baidu_json_data.each do |json_data|
   hospital = Hospital.where(:name=>json_data["org"]).first || Hospital.new
   hospital.name = json_data["org"]
   hospital.save
   puts "#{hospital.name} saved."
   site = Site.where(:url=>json_data["url"],:hospital_id=>hospital.id).first || Site.new
   site.domain = json_data["domain"]
   site.url = json_data["url"]
   site.icp = json_data["icp"]
   site.org = json_data["org"]
   site.hospital_id = hospital.id
   site.save
   puts "#{site.url} saved."
end

def parse_evidence(evidence_list, type, hospital_id)
  if evidence_list
    evidence_list.each do |evidence|
      unless Evidence.where(:type=>type,:hospital_id=>hospital_id,:url=>evidence["url"]).first
        evd = Evidence.new
        evd.hospital_id = hospital_id
        evd.type = type
        evd.url = evidence["url"]
        evd.title = evidence["title"]
        evd.snapshot = evidence["snapshot"]
        evd.dateline = evidence["dateline"]
        evd.save
      end
    end
  end
end

Dir.foreach(".") do |file|
  if file.include?("\.yml") && file!="example.yml"
    data = Psych.load_file("./#{file}")
    name = data["name"]
    hospital = Hospital.where(:name=>name).first || Hospital.new
    hospital.dataversion = data["dataversion"]
    hospital.guid = data["id"]
    hospital.usid = data["USID"]
    hospital.name = name
    hospital.city = data["city"]
    hospital.province = data["province"]
    hospital.address = data["address"]
    hospital.type = data["type"]
    hospital.save
    if data["location"]
      hospital.location = hospital.location || Location.new
      hospital.location.lat=data["location"]["lat"].to_f
      hospital.location.lng=data["location"]["lng"].to_f
      hospital.location.save
    end
    hospital.principal = data["principal"]
    hospital.shareholder_list = data["shareholder"].join(",")
    if data["url"]
      data["url"].each do |url|
        url = url.to_s.gsub("http://","").gsub("https://","").split("/")[0]
        site = Site.where(:url=>url).first || Site.new
        site.url = url
        site.hospital_id==hospital.id
        site.save
      end
    end
    hospital.phone_list = data["phone"].join(",")
    if data["baiduad"]
      parse_evidence(data["baiduad"]["evidence"],"baidu",hospital.id)
    end
    if data["news"]
      parse_evidence(data["news"]["evidence"],"news",hospital.id)
    end
    if data["putian"]
      parse_evidence(data["putian"]["evidence"],"putian",hospital.id)
    end
    if data["comments"]
      parse_evidence(data["comments"]["evidence"],"comment",hospital.id)
    end
    hospital.save
  end
end