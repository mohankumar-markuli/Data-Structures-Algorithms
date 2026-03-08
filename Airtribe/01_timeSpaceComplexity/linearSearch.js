function search(arr,key){
    n = arr.length
    for(let i=0; i<n; i++){
        if(arr[i] == key){
            return i;
        }
    }
    return -1;
}

const result = search([6,2,1,5,7,3],10)
console.log(result) 