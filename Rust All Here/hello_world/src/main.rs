

fn complex_code(){
    use std::str::FromStr;
    use std::env;

    let mut arguments = Vec::new();

    for arg in env::args().skip(1){
        arguments.push(u64::from_str(&arg).expect("error Era esperado um valor 64 int"));
    }

    if arguments.len() == 0{
        eprintln!("é necessário pelo menos 2 valores.");
        std::process::exit(1)
    }

    let mut d = arguments[0];
    for m in &arguments[1..]{
        println!("m é {}", *m); // copia o valor
        println!("m é {}", &m); // empresta o valor
        d = gdc(d, *m)
    }

    println!("O valor retornado da op Complex_Code foi: {} de {:?}", d, arguments)   
    
}



fn gdc(mut n: u64, mut m: u64) -> u64{
    assert!(n != 0 && m != 0);
    while m != 0 {
        if m < n {
            let t: u64 = m;
            m = n;
            n = t;
        }
        m = m % n;

    }
    println!("{} {}", m, n);
    return n
}



fn main() {
    println!("Hello, world!");
    // println!("\n\n{}", gdc(21, 22));
    complex_code()
}






// Test Area

#[test]
fn gdc_checker(){
    assert_eq!(gdc(21, 22), 1);
    assert_eq!(gdc(2 * 3 * 5 * 11 * 17, 3 * 7 * 11 * 13 * 19), 3 * 11);
}

