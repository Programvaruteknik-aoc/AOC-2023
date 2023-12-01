defmodule Day1Test do
  import Day1
  use ExUnit.Case


  @simpledoc "Part 1"

  test "Part 1 example returns correctly" do
    assert part1("test/test_input/day1_part1.txt") == 142
  end

  test "Part 1 should find no digits" do
    assert find_digits("nodigits") == []
  end

  test "Part 1 should find single digits" do
    assert find_digits("treb7uchet") == ["7"]
  end

  test "Part 1 should find first and last digits" do
    assert find_digits("1abc2") == ["1", "2"]
  end

  test "Part 1 should find surrounded digits" do
    assert find_digits("pqr3stu8vwx") == ["3", "8"]
  end

  test "Part 1 should find multiple digits" do
    assert find_digits("a1b2c3d4e5f") == ["1", "2", "3", "4", "5"]
  end


  @simpledoc "Part 2"

  test "Part 2 example returns correctly" do
    assert part2("test/test_input/day1_part2.txt") == 281
  end

  test "Part 2 should find no digits or tokens" do
    assert find_digits_including_tokens("nodigits") == []
  end

  test "Part 2 should find tokens" do
    assert find_digits_including_tokens("eightwothree") == ["8", "2", "3"]
  end

  test "Part 2 should find mixed tokens and digits - tokens last" do
    assert find_digits_including_tokens("two1nine") == ["2", "1", "9"]
  end

  test "Part 2 should find surrounded digits and tokens" do
    assert find_digits_including_tokens("abcone2threexyz") == ["1", "2", "3"]
  end

  test "Part 2 should find only digits and numbers" do
    assert find_digits_including_tokens("4nineeightseven2") == ["4", "9", "8", "7", "2"]
  end

  test "Part 2 should handle overlaps" do
    assert find_digits_including_tokens("zoneight234") == ["1", "8", "2", "3", "4"]
  end


  @simpledoc "General"

  test "Should extract first and last digits" do
    assert extract_first_and_last_digits(["1", "2", "3", "4", "5"]) == 15
  end



end
