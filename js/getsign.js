function f1(l1) {
    l1 = l1.sort((a, b) => a.localeCompare(b));
    let str1 = "";
    str1 += l1.join('');
    return str1
}
