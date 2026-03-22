use std::collections::HashMap;
use std::io::{self, Write};

fn main() {
    let mut db = HashMap::new();
    loop {
        let mut command = String::new();
        io::stdin()
            .read_line(&mut command)
            .expect("Failed to read line");
        let tokens: Vec<&str> = command.split_whitespace().collect();
        match tokens.as_slice() {
            ["get", key] => match db.get(key) {
                Some(value) => println!("{}", value),
                None => println!("Key not found"),
            },
            ["set", key, value] => {
                db.insert(key.to_string(), value.to_string());
            }
            ["delete", key] => {
                db.remove(key);
            }
            ["exit"] => return,
            _ => println!("Invalid command"),
        }
        io::stdout().flush().unwrap();
    }
}