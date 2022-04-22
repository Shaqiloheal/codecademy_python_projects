weight = 41.5

# ground shipping
if weight <= 2:
  cost_ground = 20.00 + (1.50 * weight)
elif weight <= 6:
  cost_ground = 20.00 + (3.00 * weight)
elif weight <= 10:
  cost_ground = 20.00 + (4.00 * weight)
else:
  cost_ground = 20.00 + (4.75 * weight)

# premium shipping
cost_premium = 125.00

# drone shipping
if weight <= 2:
  cost_drone = (4.50 * weight)
elif weight <= 6:
  cost_drone = (9.00 * weight)
elif weight <= 10:
  cost_drone = (12.00 * weight)
else:
  cost_drone = (14.25 * weight)


print(cost_ground)
print(cost_premium)
print(cost_drone)
