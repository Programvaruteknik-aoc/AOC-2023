def find_first_number(text)
  text[/\d/]
end
def find_last_number(text)
  text.reverse[/\d/]
end
value = 0
File.readlines('./1/input.txt', chomp: true).each do |line|
  new_num = find_first_number(line) + find_last_number(line)
  value = value + Integer(new_num)
end
puts value