input = 'day22'

secrets = list(map(int, open(input).read().splitlines()))

def mix(val, secret):
  return val ^ secret

def prune(val):
  return val % 16777216

def doMagic(val):
  val = prune(mix(val * 64, val))
  val = prune(mix(val // 32, val))
  val = prune(mix(val * 2048, val))
  return val

def partOne():
  
  total = 0
  for secret in secrets:
    for _ in range(2000):
      secret = doMagic(secret)
    total += secret

  print(total)


def partTwo():
  seq_to_total = {}

  for secret in secrets:
    buyer = [secret % 10]
    for _ in range(2000):
      secret = doMagic(secret)
      buyer.append(secret % 10)
    seen = set()
    for i in range(len(buyer) - 4):
      a, b, c, d, e = buyer[i:i + 5]
      seq = (b - a, c - b, d - c, e - d)
      if seq in seen: continue
      seen.add(seq)
      if seq not in seq_to_total: seq_to_total[seq] = 0
      seq_to_total[seq] += e

  print(max(seq_to_total.values()))

partOne()
partTwo()