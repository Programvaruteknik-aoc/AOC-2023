defmodule Day1 do
  import Aoc2023

  @doc """
  Solves part1 by reading lines from an input file, extracting first and last numbers,
  concatenating them, and summing them.
  """
  def part1(input) do
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&extract_numbers/1)
    |> Enum.map(&concatenate_numbers/1)
    |> Enum.sum()
  end

  @doc """
  Solves part2 by doing the same, but considering number tokens as valid numbers too.
  """
  def part2(input) do
    IO.puts("Not implemented #{input} ")
    stream_lines(input)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&extract_numbers_including_tokens/1)
    |> Enum.map(&IO.inspect/1)
    |> Enum.sum()

  end

  defp extract_numbers(line) do
    case Regex.scan(~r/\d/, line) do
      [first_num | _] = matches ->
        last_num = List.last(matches)
        {hd(first_num), hd(last_num)}
        _ -> {0, 0}
      end
    end

  defp concatenate_numbers({first, last}) do
    String.to_integer(first <> last)
  end

  defp extract_numbers_including_tokens(line) do
    number_token_values = %{
      "one" => "1", "two" => "2", "three" => "3",
      "four" => "4", "five" => "5", "six" => "6",
      "seven" => "7", "eight" => "8", "nine" => "9"
    }
    number_token_or_digit = ~r/(?:one|two|three|four|five|six|seven|eight|nine|\d)/
    Regex.scan(number_token_or_digit, line)
    |> List.flatten()
    # |> Enum.map(&IO.inspect/1)
    |> Enum.map(fn token ->
      Map.get(number_token_values, token, token)
    end)
    |> extract_first_and_last_digits()
  end

  # defp extract_first_and_last_digits(list) do
  #   case list do
  #     [first | _] = matches ->
  #       last = List.last(matches)
  #       String.to_integer(first <> last)
  #     _ -> 0
  #   end
  # end

  defp extract_first_and_last_digits(list) do
    case list do
      [single] ->
        # If there's only one digit, duplicate it for both first and last
        String.to_integer(single <> single)
        # single <> single
      [first | _] = matches ->
        # If there are multiple digits, take the first and last as usual
        last = List.last(matches)
        String.to_integer(first <> last)
        # first <> last
      _ ->
        0
    end
  end


end
