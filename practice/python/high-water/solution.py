def high_water_marks(readings):
  result = []
  current_max = float('-inf')  # handles negative numbers correctly
  for r in readings:
    if r > current_max:
      current_max = r
    result.append(current_max)
  return result
