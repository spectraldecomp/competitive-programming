defmodule Solution do
  @spec is_subsequence(s :: String.t, t :: String.t) :: boolean
  def is_subsequence(s, t) do
    s = String.graphemes(s)
    t = String.graphemes(t)

    is_subsequence(s, t, true)
  end

  def is_subsequence(s, t, isnt_string) do

    # Empty case checking
    case s do
      [] ->
        true
      x ->
        case t do
          [] ->
            false
          y ->
            [t_h | t_t] = t
            [s_h | s_t] = s

            if t_h == s_h do
              is_subsequence(s_t, t_t, true)
            else
              is_subsequence(s, t_t, true)
            end
        end
    end
end
end