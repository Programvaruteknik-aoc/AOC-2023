defmodule Day2Test do
  import Day2
  use ExUnit.Case


  @simpledoc "Part 1"

  test "part 1 should return correctly" do
    assert part1("test/test_input/day2_part1.txt") == 8
  end

  test "should return parsed game" do
    assert parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") ==
      %{id: 1, sets: [
        [{:blue, 3}, {:red, 4}],
        [{:red, 1}, {:green, 2}, {:blue, 6}],
        [{:green, 2}]
      ]}
  end

  test "should return parsed set" do
    assert parse_set("3 blue, 4 red") == [{:blue, 3}, {:red, 4}]
  end

  test "should return parsed cube" do
    assert parse_cubes("3 blue") == {:blue, 3}
  end

  test "should return if a move is possible" do
    assert is_possible(%{id: 1, sets: [
      [{:blue, 3}, {:red, 4}],
      [{:red, 1}, {:green, 2}, {:blue, 6}],
      [{:green, 2}]
    ]}) == true
  end


  @simpledoc "Part 2"

  test "should return minimum cubes" do
    assert minimum_cubes(%{id: 1, sets: [
      [{:blue, 3}, {:red, 4}],
      [{:red, 1}, {:green, 2}, {:blue, 6}],
      [{:green, 2}]
    ]}) == %{red: 4, green: 2, blue: 6}
  end

  test "should return power of set" do
    assert power_of_set(%{red: 4, green: 2, blue: 6}) == 48
  end

end
