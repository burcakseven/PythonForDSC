import time
from datetime import date

today = date.today().strftime("%b %d %Y")
second = time.time()
second_f = f"{second:,.4f}"
second_s = f"{second:.2e}"
print(f"Seconds since January 1, 1970: {second_f} or {second_s} in scientific notation")
print(today)

