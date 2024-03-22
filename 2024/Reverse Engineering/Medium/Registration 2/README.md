## Registration 2

#### Challenge Difficulty: Medium
#### Topic: Pattern, XOR
#### Author: d151nt3gr4t0r

The challenge provides us with a compiled binary. We can use IDA / Ghidra or radare 2 to decompile the binary. Once decompiled we can inspect the code and identify the main function.


```c
int main(){
  char registrationKey[30];
  printf("Thank you for using our application!\n");
  printf("In order to use our application to it's maximum extend please supply the registration key you received with your purchase\n");
  do{
    scanf("%30s", &registrationKey);
    
    if(checkKey(registrationKey)){
      printf("Thank you for purchasing our software!\n Your flag is: csc{%s}\n", registrationKey);
      break;
    }
    else{
      printf("Registration failed. Please try again!\n");
      }
  }while(true);

  return 0;
}
```

By the looks of it, the application performs some verifications on the key. 

```c
bool checkKey(char* registrationKey){
  if(!checkLength(registrationKey)) return false;
  if(!checkPattern(registrationKey, strlen(registrationKey))) return false;
  if(!final(registrationKey, strlen(registrationKey))) return false;
  return true;
}
```

The checkKey function first, checks the length (Length needs to be 29 characters long), then checks its pattern and then it finally checks one final thing. (Final function)

```c
int myarr[] = {75,62,75,91,87,50,56,102,75,63,59,50,84,63,63,75,81,50,63,73,63,89,100,50,87,59,59,59,91,15};

bool final(char* input, int size){
  char arr[size];

  for(int i = 0; i < 30; i++){
    arr[i] = myarr[i] ^ 5;
    arr[i] -= 10;
    if(arr[i] != input[i]) return false;
  }

  return true;
}
```

The final function seems to be performing some steps to decrypt the global array and match it to the input. Adjusting this code a bit can help us decrypt the full flag.

```python
flag = "csc{"
array = [75,62,75,91,87,50,56,102,75,63,59,50,84,63,63,75,81,50,63,73,63,89,100,50,87,59,59,59,91,15]
for num in array:
    num ^= 5
    num -= 10
    flag += chr(num)
flag += '}'
print(flag)
```

The decrypted flag is: csc{D1DTH-3YD04-G00DJ-0B0RW-H444T}