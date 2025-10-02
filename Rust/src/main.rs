// Adicionar função de formatação de saída

use std::io;

fn permited_number(number: i64, base: i64) -> bool {
    let number_str = number.to_string();
    for c in number_str.chars() {
        if c.to_digit(10).unwrap() >= base as u32 {
            return false;
        }
    }
    true
}

fn digit_to_char(d: u32) -> char {
    if d < 10 {
        (b'0' + d as u8) as char
    } else {
        (b'A' + (d - 10) as u8) as char
    }
}

fn convert_any_binary_base(number: i64, base1: i64, base2: i64) -> String {
    //create variables
    let mut result1 = String::new();
    let mut result2 = String::new();
    

    let pot = base1.trailing_zeros();
    let count = base2.trailing_zeros();

    let number_str: Vec<char> = number
        .to_string()
        .chars()
        .rev()
        .collect::<String>()
        .chars()
        .collect();
    let chars: Vec<char> = result1.chars().rev().collect::<String>().chars().collect();

    // step 1
    if !permited_number(number, base1){
        panic!("Erro: O número {} não é permitido na base {}.", number, base1);	
    }

    // step 2
    for i in number_str {
        result1.push_str(&format!(
            "{:0>width$}",
            format!("{:b}", i.to_digit(10).unwrap()),
            width = pot as usize
        ));
    }

    // step 3
    for chunk in chars.chunks(count as usize) {
        // Converte o chunk de caracteres binários para uma String
        let chunk_binary_str: String = chunk.iter().collect();
        
        // Converte a String binária para um número inteiro (u32)
        let chunk_value = u32::from_str_radix(&chunk_binary_str, 2).expect("Falha ao converter chunk binário para inteiro");
        
        // Converte o valor para a base desejada (base2)
        // let digit = format!("{:X}", chunk_value); // Usando hexadecimal como exemplo
        // Ou, para bases arbitrárias (implementação mais complexa seria necessária)
        
        result2.push(digit_to_char(chunk_value));
    }


    result2
}

// FUNCTION MAIN
fn main() {
    //testes
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler entrada");

    println!("Hello, Rust! You entered: {}", input.trim());

    println!("{}", format_args!("{:b}", 8));
    println!("{}", format_args!("{:b}", 87));
}
