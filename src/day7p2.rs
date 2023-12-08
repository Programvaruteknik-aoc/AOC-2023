use std::cmp::Ordering;
use std::collections::HashMap;
use crate::helper::Data;

fn find_value_for_card(card:char) -> u32{
    let values:Vec<char> = vec!['X','J','2','3','4','5','6','7','8','9','T','J','Q','K','A'];
    values.iter().enumerate().find(|&(_idx, &val)| val == card).unwrap().0 as u32
}
fn find_occurrences(hand:&str, card:char) -> u32{
    hand.chars().into_iter().filter(|c|*c == card).count() as u32
}
fn find_value_by_card(hand1:&str, hand2:&str) -> (u32,u32){
    let mut index = 0;
    let mut a = hand1.chars().nth(index).unwrap();
    let mut b = hand2.chars().nth(index).unwrap();
    while a == b {
        a = hand1.chars().nth(index).unwrap();
        b = hand2.chars().nth(index).unwrap();
        index += 1;
    }
    let tup = (find_value_for_card(a),find_value_for_card(b));
    return tup;
}
fn rearrange(duplicate: &mut Vec<(&str, u32)>){
    duplicate.sort_by(|a, b| {
        let values = find_value_by_card((*a).0,(*b).0);
        let a_val = values.0;
        let b_val = values.1;
        if a_val < b_val {
            return Ordering::Less;
        } else if a_val > b_val {
            return Ordering::Greater;
        } else {
            return Ordering::Equal;
        }
    });
}
fn find_rank(hand:&str) -> (&str, u32,u64) {
    let values:Vec<char> = vec!['X','X','2','3','4','5','6','7','8','9','T','J','Q','K','A'];
    let index = values.iter().enumerate().find(|&(_idx, &val)| val == 'K').unwrap();
    let mut hand_rank:HashMap<char,u32> = HashMap::new();
    let counts = hand.chars().into_iter().map(|c|c.clone()).for_each(|c|{
        let occ = find_occurrences(hand, c);
        hand_rank.insert(c,occ);
    });

    let mut pairs: Vec<_> = hand_rank.iter().collect();
    pairs.sort_by(|a, b| b.1.cmp(a.1));

    // for (key, value) in pairs {
    //     println!("{}: {}", key, value);
    // }
    let has_j = hand.find('J').unwrap_or_else(|| usize::MIN) as u64;
    let highest_pair = pairs.get(0).unwrap().clone();
    let next_highest_pair = pairs.get(1).unwrap_or_else(||{
        &(&'Y', &0)
    }).clone();
    let next_highest = *next_highest_pair.1;
    let highest = *highest_pair.1;
    let mut rank:u64 = 0;
    match highest {
        5 => {
            // Five of a kind
            rank = 7;
        }
        4 => {
            // Four of a kind
            rank = 6;
            if has_j == 1 {
                rank = 7;
            }
        }
        3 => {
            if  next_highest == 2{
                // Full house
                rank = 5;
                if has_j == 1 {
                    rank = 6;
                }
                else if has_j == 2{
                    rank = 7;
                }
            }
            else{
                // Three of a kind
                rank = 4;
            }

        }
        2 => {
            if next_highest == 2{
                // Two pairs
                rank = 3;
                if has_j == 1 {
                    rank = 4;
                }
                else if has_j == 2{
                    rank = 6;
                }
            }
            else{
                // One Pair
                rank = 2;
                if has_j == 1{
                    rank = 4
                }

            }

        }
        1 => {
            rank = 1;
            if has_j > 0 {

            }
        }
        _ => { rank = 0;}
    }
    return (hand, rank as u32, 0);
}

pub fn start(){
    let data:Data = Data::new(7,2);
    let mut hands:HashMap<&str,&str> = HashMap::new();
    let mut ranks:HashMap<&str,u32> = HashMap::new();
    data.example.lines().for_each(|line|{
        let kv = line.split_once(" ").unwrap();
        hands.insert(kv.0,kv.1);
    });

    let mut ranked_hands:Vec<(&str,u32,u64)> = Vec::new();
    for hand in hands{
        let mut ranked = find_rank(hand.0);
        ranked.2 = hand.1.parse::<u64>().unwrap();
        ranked_hands.push(ranked);
        //println!("{}:{} -> {}:{}",hand.0,hand.1,ranked.0,ranked.1);
    }
    ranked_hands.sort_by(|a, b| b.1.cmp(&a.1));
    let highest = ranked_hands.iter().max_by_key(|&(_,value,_)|value).unwrap().1;
    for index in 1..highest {
        let start = ranked_hands.iter().position(|&(_, v, _)| v == index).unwrap_or(0);
        let end = ranked_hands.iter().rposition(|&(_, v, _)| v == index).map_or(start, |i| i + 1);
        ranked_hands[start..end].sort_by(|a, b|{
            let values = find_value_by_card((*a).0,(*b).0);
            let a_val = values.0;
            let b_val = values.1;
            if a_val < b_val {
                return Ordering::Greater;
            } else if a_val > b_val {
                return Ordering::Less;
            } else {
                return Ordering::Equal;
            }
        });
    }
    // Invers?
    //ranked_hands.sort_by(|a, b| a.cmp(b)); // Descending order
    let ranked_reverse:Vec<&(&str,u32,u64)> = ranked_hands.iter().rev().collect();

    let mut sum = 0;
    let mut counter = 1;
    let mut info:String = String::from("");
    for (key, value, bid) in ranked_reverse{
        println!("Hand:{}: Rank:{} Bid:{} Preorder:{}", key, counter,bid,value);
        info = format!("{} {} * {} + ",info ,bid,counter);
        sum += counter*bid;
        counter += 1;
    }
    println!("{}",info);
    println!("Sum:{}",sum);
}
// 765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5
// 765 * 1 + 28 * 2 + 220 * 3 + 483 * 4 + 684 * 5 +
/*
32T3K
KTJJT
KK677
T55J5
QQQJA

 Hand:32T3K: Rank:1 Bid:765 Preorder:2
Hand:KTJJT: Rank:2 Bid:220 Preorder:3
Hand:KK677: Rank:3 Bid:28 Preorder:3
Hand:QQQJA: Rank:4 Bid:483 Preorder:4
Hand:T55J5: Rank:5 Bid:684 Preorder:4

Hand:32T3K: Rank:1 Bid:765 Preorder:2
Hand:KTJJT: Rank:2 Bid:220 Preorder:3
Hand:KK677: Rank:3 Bid:28 Preorder:3
Hand:T55J5: Rank:4 Bid:684 Preorder:4
Hand:QQQJA: Rank:5 Bid:483 Preorder:4
low 253269737
low 253271833
253269996
253264768
253273054
 */