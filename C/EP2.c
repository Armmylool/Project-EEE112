int fun1()
{ 
     return 1;
}

void fun2()
{
   int x;
}

int main() {

  int fun1=fun1;
  int fun2=fun2;

    printf("%d\n%d",fun1,fun2);
    return 0;
}   