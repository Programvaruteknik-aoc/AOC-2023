value = 0
numbers = {
  /one/ => 'one1one',
  /two/ => 'two2two',
  /three/ => 'three3three',
  /four/ => 'four4four',
  /five/ => 'five5five',
  /six/ => 'six6six',
  /seven/ => 'seven7seven',
  /eight/ => 'eight8eight',
  /nine/ => 'nine9nine'
}

File.readlines('./1/input.txt', chomp: true).each do |line|
  numbers.each { |regex, digit| line.gsub!(regex, digit) }
  value = value + Integer(line[/\d/] + line.reverse[/\d/])
end

puts value