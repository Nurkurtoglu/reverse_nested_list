def reverse_nested_list(lst):
    # Ana listeyi tersine çeviriyoruz
    lst = lst[::-1]
    # İç listeleri de tersine çevirmek için her elemanı kontrol ediyoruz
    for i in range(len(lst)):
        if isinstance(lst[i], list):  # Eğer eleman bir liste ise
            lst[i] = lst[i][::-1]     # O listeyi de tersine çeviriyoruz
    return lst

# Örnek kullanım
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_nested_list(input_list)
print(output)  # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]
