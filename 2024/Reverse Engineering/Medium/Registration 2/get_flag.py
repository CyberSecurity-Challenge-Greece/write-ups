# int myarr[] = {75,62,75,91,87,50,56,102,75,63,59,50,84,63,63,75,81,50,63,73,63,89,100,50,87,59,59,59,91,15};

# bool final(char* input, int size){
#   char arr[size];

#   for(int i = 0; i < 30; i++){
#     arr[i] = myarr[i] ^ 5;
#     arr[i] -= 10;
#     if(arr[i] != input[i]) return false;
#   }

#   return true;
# }
flag = "csc{"
array = [75,62,75,91,87,50,56,102,75,63,59,50,84,63,63,75,81,50,63,73,63,89,100,50,87,59,59,59,91,15]
for num in array:
    num ^= 5
    num -= 10
    flag += chr(num)
flag += '}'
print(flag)