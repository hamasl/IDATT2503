fn replace_sign(input: String , to_be_replaced: &str, replace_with: &str) -> String{
    let mut str = input.clone();
    let mut index = 0;
    while index < str.chars().count() {
        let index_wrapper = &str[index..].find(to_be_replaced).map(|i| i+index);
        match index_wrapper {
            Some(x) => {
                index = x
                //last substring goes from str.length() to str.length() in case the last character is a charcater to be replaced
                //however substr returns an empty string if the start index is equal to the strings length, therefore this does not matter
                str = &str[0..index] + replace_with + &str[to_be_replaced.length()+index..str.length()];
                //Increasing (or decreasing) by the difference of the number of characters to be inserted and the number to be removed
                index += replace_with.length() - to_be_replaced.length();
            },
            None => {
                //breaks while loop condition
                index = str.length();
            },
        }
        if index_wrapper == None {
            
        }
        else {
            
        }
    }
    return str;
}

fn convert(input: String) -> String{
    return replace_sign(replace_sign(replace_sign(input, "&", "&amp"), "<", "&lt"), ">", "&gt");
}

fn main(){
    let input = String::from("&lorem ip&sum < > <zx>");
    //let input = "&lorem ip&sum < > <zx>".to_string();

    //let input = "&lorem ip&sum < > <zx>";
    println!("{} converted to: {}", input, convert(input));
    //println!("{}", &input[3..5])
}