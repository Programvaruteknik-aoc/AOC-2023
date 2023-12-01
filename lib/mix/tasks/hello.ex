defmodule Mix.Tasks.Hello do
  use Mix.Task

  @shortdoc "Test for executing mix tasks"
  def run(_args) do
    IO.puts("Hello " <> Atom.to_string(Aoc2023.hello))
  end

end
