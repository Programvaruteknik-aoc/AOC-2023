use std::io::BufRead;
use std::ops::{Range, RangeBounds};
use std::slice::Iter;
use crate::helper::Data;

#[derive(Default)]
struct SeedMap{
    pub name:String,
    pub destinations:Vec<Range<u64>>,
    pub sources:Vec<Range<u64>>
}
impl SeedMap {
    pub fn new(name:&str) ->  SeedMap {
        SeedMap{
            name:String::from(name),
            destinations: vec![],
            sources: vec![],
        }
    }
    pub fn passthrough(&self, seed:u64) -> u64 {

        let dolk = self.sources
            .iter()
            .enumerate()
            .find(|source|source.1.contains(&seed));
        match dolk {
            None => {
                // println!("Seedmap out:{}",10);
                seed
            }
            Some(dolk) => {
                let dist = seed - dolk.1.start;
                let mut_seed = self.destinations.get(dolk.0).unwrap().start + dist;
                // println!("Seedmap out:{}",mut_seed);
                return mut_seed;
            }
        }
    }
    pub fn print(&self){

    }
}

#[derive(Default)]
struct Entry{
    pub seeds:Vec<u64>,
    pub maps:Vec<SeedMap>,
    pub locations:Vec<u64>
}
impl Entry {
    pub fn new(seeds:Vec<u64>) ->  Entry {
        Entry{ seeds, maps: vec![], locations:vec![] }
    }
    fn rightmost_chars(s: &str, n: usize) -> String {
        let chars: Vec<char> = s.chars().collect();
        if n > chars.len() {
            return s.to_string();
        }
        chars[chars.len() - n..].iter().collect()
    }
    pub fn go(&mut self){
        let seed_clone = self.seeds.clone();
        let mut c = 0;
        let total = self.seeds.len();
        for seed in seed_clone {
            let mut left = total - c;
            if left.to_string().ends_with("000000"){

            println!("Entering:{}",left);
            }
            c += 1;
            self.passthrough(seed);
        }
    }
    pub fn passthrough(&mut self, seed:u64) -> u64 {
        let mut mut_seed:u64 = seed.clone();
        self.maps.iter().for_each(|map|{
            // println!("[{}]", map.name);
            // println!("Entry In:{}",mut_seed);
            mut_seed = map.passthrough(mut_seed);
            // print!("Out:{}",mut_seed);
            // println!();
        });
        self.locations.push(mut_seed);
        mut_seed
    }
    pub fn print(&self){

    }
}

fn parse_numbers(num_str:&str) -> Vec<u64>{
    num_str.trim()
        .split_whitespace()
        .filter_map(|s| s.parse::<u64>().ok())
        .collect()
}

pub fn start(){
    let data:Data = Data::new(5,2);
    let mut entries:Vec<Entry> = Vec::new();
    let mut lines = data.input.lines();

    while let Some(seed_line) = lines.next() {
        // Seeds
        let seeds_str: &str = seed_line
            .split_once(":")
            .map_or_else(|| "",|(_, numbers)|numbers);
        //let seeds:Vec<u64> = parse_numbers(seeds_str);
        let seeds_ranges:Vec<u64> = parse_numbers(seeds_str);
        // for seeds_range in seeds_ranges {
        //     println!("Seed range:{}",seeds_range);
        // }
        let mut ranges: Vec<Range<u64>> = seeds_ranges
            .chunks(2)
            .filter_map(|chunk| {
                if chunk.len() == 2 {
                    Some(chunk[0]..(chunk[0] + chunk[1]))
                } else {
                    None // Ignore incomplete chunks
                }
            })
            .collect();

        // println!("Ranges count:{}",ranges.len());
        let mut seeds:Vec<u64> = Vec::new();
        ranges.iter().for_each(|r|{
            let start = r.clone().start;
            let end = r.clone().end;
            // println!("Start {}",start);
            // println!("end {}",end);
            let t_range = start..end;
            for num in t_range {
                // println!("Num:{}",num);
                //println!("Start:{} count:{}",&r.start,99);
                seeds.push(num);
            }
        });
        println!("Seeds: {}",seeds.len());
        for seed in &seeds {
            // print!("{} ",*seed);
        }
        let mut entry:Entry = Entry::new(seeds);
        lines.next();
        // seeds.iter().for_each(|s|{
        //     print!("{} ",s);
        // });

        // Maps
        for i in 0..7 {
            let mut line = lines.next().unwrap();
            let name = line;
            // println!("Mapname:{}",name);
            let mut seedMap:SeedMap = SeedMap::new(name);
            line = lines.next().unwrap();
            while line != "" {
                let range_numbers:Vec<u64> = parse_numbers(line);
                let d:u64 = *range_numbers.get(0).unwrap();
                let s:u64 = *range_numbers.get(1).unwrap();
                let l:u64 = *range_numbers.get(2).unwrap();
               //println!("Seedmap:[{}]",seedMap.name);
                let destination:Range<u64> = d..(d+l);
                let source:Range<u64> = s..(s+l);
                seedMap.destinations.push(destination);
                seedMap.sources.push(source);
                line = lines.next().unwrap_or_else(||"");
            }
            entry.maps.push(seedMap);
        }
        entry.go();
        entry.locations.sort();
        println!("{}",entry.locations.get(0).unwrap());
    }
}