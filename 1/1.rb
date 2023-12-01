value = 0
File.readlines('./1/input.txt', chomp: true).each do |line|
  new_num = line[/\d/] + line.reverse[/\d/]
  value = value + Integer(new_num)
end
puts value