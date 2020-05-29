

function generateSignGetbx(params, bxEvn, partner) {
    // 把{a: 1, b:2}变成 ['a=1', 'b=2']
    let parArr = []
    for (var key in params) {
        // 把所有key值变成小写
        const newkey = key.toLowerCase()
        // 为空的值 不参与生成签名
        if (Array.isArray(params[key])) {
            params[key] = params[key].sort((a, b) => a.localeCompare(b));
            params[key] = params[key].join('');
            parArr.push(newkey + '=' + params[key])
        } else if (params[key] !== '') {
            parArr.push(newkey + '=' + params[key])
        }
    }
    parArr.push('partner=' + partner)
    if (user.getToken()) {
        parArr.push('utoken=' + user.getToken())
    }

    //排序
    parArr = parArr.sort();
    // 把['a=1', 'b=2'] 变成 'a=1$b=2'
    let str = ""
    parArr.forEach((value) => {
        str += value + '&'
    })
    str = str.slice(0, str.length - 1)
    str += bxEvn
    return md5(str)

}

function generateSignPost(params, bxEvn, partner) {
  var token = user.getToken() ? "utoken=" + user.getToken() + "&" : '';
  let str = 'partner=' + partner + '&' + token + params
  str += bxEvn
  return md5(str)
}



// 则先对密码作MD5算法获取摘要，并把获取的salt拼接到摘后再次作MD5算法，把摘要作为密码传入，30秒内有效，解密一次后失效
NSString *salt = [response.AppendData valueForKey:@"Salt"];
NSString *md5PassWord = [passWord md5String];
if (salt && ![salt isEqual:[NSNull null]] && salt.length) {
    md5PassWord = [[md5PassWord stringByAppendingString:salt] md5String];
}