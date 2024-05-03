defmodule Solution do
  @spec largest_altitude(gain :: [integer]) :: integer
  def largest_altitude(gain) do
    case gain do
      x ->
        largest_altitude(x, 0, 0)
      [] ->
        0
    end
  end

  def largest_altitude([h | t], altitude, max) do
    if altitude+h > max do
      largest_altitude(t, altitude+h, altitude+h)
    else
      largest_altitude(t, altitude+h, max)
    end
  end

  def largest_altitude([], altitude, max) do
    if altitude > max do
      altitude
    else
      max
    end
  end
end