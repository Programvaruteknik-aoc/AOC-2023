defmodule Day1 do
  import Aoc2023

  @doc """
  Solves part1 by reading lines from an input file, extracting first and last numbers,
  concatenating them, and summing them.
  """
  def part1(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&find_digits/1)
    |> Enum.map(&extract_first_and_last_digits/1)
    |> Enum.sum()
  end

  @doc """
  Solves part2 by doing the same, but considering number tokens as valid numbers too.
  """
  def part2(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&find_digits_including_tokens/1)
    |> Enum.map(&extract_first_and_last_digits/1)
    |> Enum.sum()
  end

  def find_digits(line) do
    Regex.scan(~r/\d/, line)
    |> List.flatten()
  end

  def find_digits_including_tokens(line) do
    number_token_values = %{
      "one" => "1", "two" => "2", "three" => "3",
      "four" => "4", "five" => "5", "six" => "6",
      "seven" => "7", "eight" => "8", "nine" => "9"
    }

    number_token_or_digit = ~r/(?=(one|two|three|four|five|six|seven|eight|nine|\d))/

    Regex.scan(number_token_or_digit, line)
    |> List.flatten()
    |> Enum.reject(fn match -> match == "" end)
    |> Enum.map(fn token -> Map.get(number_token_values, token, token) end)
  end

  def extract_first_and_last_digits(digits) do
    case digits do
      [first | _] = matches ->
        last = List.last(matches)
        String.to_integer(first <> last)
      _ -> 0
    end
  end
end
