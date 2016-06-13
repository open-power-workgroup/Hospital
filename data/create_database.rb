require 'sequel'
require 'sqlite3'

if File.exist?("./hospital.db")
  `rm ./hospital.db`
end

DB = Sequel.sqlite("./hospital.db")

DB.create_table :locations do
  primary_key :id
  Integer :hospital_id
  Float :lat
  Float :lng
end

DB.create_table :sites do
  primary_key :id
  Integer :hospital_id
  String :name
  String :domain
  String :url
  String :auth
  String :icp
  String :org
end

DB.create_table :evidences do
  primary_key :id
  Integer :hospital_id
  String :type
  String :url
  String :title
  String :snapshot
  String :dateline
end

DB.create_table :hospitals do
  primary_key :id
  String :dataversion
  Datetime :created
  Datetime :updated
  String :guid
  String :usid
  String :name
  String :city
  String :province
  String :address
  String :type
  String :bdv
  String :desc
  Integer :location_id
  String :principal
  String :shareholder_list
  String :phone_list
end