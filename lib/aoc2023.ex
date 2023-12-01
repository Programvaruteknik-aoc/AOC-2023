defmodule Aoc2023 do
  @moduledoc """
  Documentation for `Aoc2023`.
  """

  @doc """
  Streams lines from a file
  """
  def stream_lines(file_name) do
    file_name
    |> File.stream!()
  end

  @doc """
  Reads the passed input file as a binary data object.
  """
  def read_file(file_name) do
    File.read(file_name)
  end

  @doc """
  Hello aoc2023.

  ## Examples

      iex> Aoc2023.hello()
      :aoc2023

  """
  def hello do
    :aoc2023
  end
end
