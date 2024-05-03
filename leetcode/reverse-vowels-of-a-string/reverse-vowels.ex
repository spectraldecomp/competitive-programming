defmodule Solution do
  @spec reverse_vowels(s :: String.t) :: String.t
  def reverse_vowels(s) do
    to_string(merge(String.graphemes(s), rev(String.graphemes(s), [])))
  end

  def rev([h | s], t) do
    case h do
      h when h in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] ->
        rev(s, [h | t])
      _ -> rev(s, t)
    end
  end

  def rev([], t) do
    t
  end

  def merge([h | s], [v | t]) do
    case h do
      h when h in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] ->
        [v | merge(s, t)]
      _ ->
        [h | merge(s, [v | t])]
    end
end

  def merge(x, []) do
    x
  end






end