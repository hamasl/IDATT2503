fn main(){
    let input = String::from("&lorem ip&sum < > <zx>");
    let converted = input.replace("&", "&amp").replace("<", "&lt").replace(">", "&gt");

    println!("{} converted to: {}", input, converted);
}