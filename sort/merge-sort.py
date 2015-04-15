import random

def merge_sort(arr, d = 0):
    l = len(arr)
    if l == 1:
        return arr
    else:
        left = merge_sort(arr[:l//2], d + 1)
        right = merge_sort(arr[l//2:], d + 1)
        merged = []
        while len(left) > 0 and len(right) > 0:
            src = left if left[0] < right[0] else right
            merged.append(src[0])
            del src[0]
        return merged + left + right

def merge_sort2(arr):
    def merge(a, b, d):
        print(("    " * (d + 1)) + "Merge -> " + str(a) + ", " + str(b))
        r = []
        while len(a) > 0 and len(b) > 0:
            s = a if a[0] < b[0] else b
            r.append(s[0])
            del s[0]
        return r + a + b

    def split(arr, d = -1):
        d += 1
        print(("    " * d) + "Split -> " + str(arr))
        l = len(arr)
        if l == 1:
            return arr
        elif l == 2:
            return merge([arr[0]], [arr[1]], d)
        else:
            left = arr[:l//2]
            right = arr[l//2:]
            return merge(split(left, d), split(right, d), d)

    return split(arr)

print(merge_sort([ random.randint(-99,99) for _ in range(15) ]))
