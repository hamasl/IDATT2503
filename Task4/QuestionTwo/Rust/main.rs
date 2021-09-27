fn edit(input: &str) -> String{
    return input.replace("&", "&amp").replace("<", "&lt").replace(">", "&gt")
}

fn main(){
    let input = String::from("&lorem ip&sum < > <zx>");
    let input2 = String::from("if 2 < 1 && 3 > 4");
    let input3 = String::from("else is 1<10 && 23 > 8");

    println!("{} converted to: {}", input, edit(&input));
    println!("{} converted to: {}", input2, edit(&input2));
    println!("{} converted to: {}", input3, edit(&input3));
}