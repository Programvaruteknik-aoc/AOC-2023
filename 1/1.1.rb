value = 0
File.readlines('./1/input.txt', chomp: true).each do |line|
  value = value + Integer(line[/\d/] + line.reverse[/\d/])
end
puts value