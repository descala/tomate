#!/usr/bin/ruby

prefixe = File.basename($0)

## monta el windows xp virtual
#`gvfs-mount smb://kvmxp/tasaciones/`
#
## el GVFS per programes POSIX (l'usuari ha de ser membre del grup fuse) 
#carpeta = "~/.gvfs/tasaciones\\ a\\ kvmxp/#{Dir.pwd.split('/').last}"

begin
  nom = prefixe.split('-').first
rescue
  nom = 'montage'
end

begin
  c, f = prefixe.split('-')[1].split('x')
rescue
  c = f = 1
end

columnes = c.to_i
files = f.to_i

# han de tenir les proporcions de 991/1402.0 => 0.7068
# p.e. 1414 x 2000
x = (1414.0-5*columnes*2)/columnes
y = (2000.0-5*files*2)/files

`mkdir -p .editor`

cmd = "montage -density 300 -units PixelsPerInch '#{ARGV.join("' '")}' -geometry #{x}x#{y}+5+5 -tile #{columnes}x#{files} .editor/#{nom}.jpg"
puts cmd
`#{cmd}`

cmd = "mogrify +profile '!exif,*' -density 99x105 -comment 'LEAD Technologies Inc. V1.01' -geometry 991x1402\\> -depth 8 -quality 25 .editor/#{nom}*.jpg"
puts cmd
`#{cmd}`

#`mkdir -p #{carpeta}`
#cmd = "cp .editor/#{nom}*.jpg #{carpeta}"
#puts cmd
#`#{cmd}`
