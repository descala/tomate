#!/usr/bin/ruby

require 'open-uri'
require 'openssl'

OpenSSL::SSL::VERIFY_PEER = OpenSSL::SSL::VERIFY_NONE

def high
  w="https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCConCiud.aspx?del=8&mun=306&UrbRus=U&RefC={r}&Apenom=&esBice=&RCBice1=&RCBice2=&DenoBice="

  open("llista_resfs_cadastrals.txt").each do |line|
    ref=line.split.first
    uri=w.gsub("{r}",ref.to_s)
    sup=open(uri).read.scan(/((\.|\d)+ m)/).first.first
    puts "#{ref},#{sup.split.first},\"#{line.split[1..-1].join(' ')}\""
  end
end

high
