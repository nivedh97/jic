let a=[6,4,1,7,3];
let b;

for(i=0;i<a.length;i++){
    for(j=0;j<a.length;j++){
        if(a[i]<a[j]){
              b=a[i];
        }
    }
}

console.log("b",b);
