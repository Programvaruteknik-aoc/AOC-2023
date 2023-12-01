defmodule Day1Test do
  import Day1
  use ExUnit.Case

  test "Part 1 example returns correctly" do
    assert part1("test/test_input/day1_part1.txt") == 142
  end

  test "Part 2 example returns correctly" do
    assert part2("test/test_input/day1_part2.txt") == 281
  end


end
