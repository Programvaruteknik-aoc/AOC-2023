from utils.util import get_input
from functools import lru_cache

class Almanac:
    def __init__(self, input) -> None:
        self.parse_input(input)
    # Destination, Source, Range
    def parse_input(self, input: list[str]) -> None:
        self.seeds = [int(x) for x in input[0].split(":")[1].split()]
        self.seed_to_soil = self.parse_map_after_keyword(input, "seed-to-soil")
        self.soil_to_fertilizer = self.parse_map_after_keyword(input, "soil-to-fertilizer")
        self.fertilizer_to_water = self.parse_map_after_keyword(input, "fertilizer-to-water")
        self.water_to_light = self.parse_map_after_keyword(input, "water-to-light")
        self.light_to_temperature = self.parse_map_after_keyword(input, "light-to-temperature")
        self.temperature_to_humidity = self.parse_map_after_keyword(input, "temperature-to-humidity")
        self.humidity_to_location = self.parse_map_after_keyword(input, "humidity-to-location")

    def parse_map_after_keyword(self, input: list[str], keyword:str) -> dict:
        map = {}
        map["destination"] = []
        map["source"] = []
        map["range"] = []
        keyword_found = False
        for line in input:
            if keyword in line:
                keyword_found = True
                continue
            elif keyword_found and line == "":
                break

            if keyword_found:
                values = line.split(" ")
                map["destination"].append(int(values[0]))
                map["source"].append(int(values[1]))
                map["range"].append(int(values[2]))
        return map

def main() -> None:
    file_input = get_input("day5/input.txt")
    print(f"Part one: {part_one(file_input)}")
    print(f"Part two: {part_two(file_input)}")


def part_one(input: list[str]) -> int:
    almanac = Almanac(input)
    locations = find_locations_for_seeds(almanac)
    return min(locations)

def part_two(input: list[str]) -> int:
    almanac = Almanac(input)
    locations = find_location_for_seed_ranges(almanac)
    return min(locations)

def find_locations_for_seeds(almanac: Almanac) -> list[int]:
    locations = []
    for seed in almanac.seeds:
        location = find_location_of_seed(almanac, seed)
        if location != -1:
            locations.append(location)
    return locations

def find_location_for_seed_ranges(almanac: Almanac) -> list[int]:
    locations = []
    for i in range(0, len(almanac.seeds), 2):
        for shift in range(almanac.seeds[i+1]):
            location = find_location_of_seed(almanac, almanac.seeds[i] + shift)
            if location != -1:
                locations.append(location)
    return locations

@lru_cache(maxsize=None)
def find_location_of_seed(almanac: Almanac, seed: int) -> int:
    soil = translate_source_to_destination(almanac.seed_to_soil, seed)
    fertilizer = translate_source_to_destination(almanac.soil_to_fertilizer, soil)
    water = translate_source_to_destination(almanac.fertilizer_to_water, fertilizer)
    light = translate_source_to_destination(almanac.water_to_light, water)
    temperature = translate_source_to_destination(almanac.light_to_temperature, light)
    humidity = translate_source_to_destination(almanac.temperature_to_humidity, temperature)
    location = translate_source_to_destination(almanac.humidity_to_location, humidity)
    return location

def translate_source_to_destination(source_destination_map: dict[str, list[int]], source_number:int) -> int:
    index = -1
    for base_index, source_start in enumerate(source_destination_map["source"]):
        if source_start <= source_number <= source_start + source_destination_map["range"][base_index]:
            index = base_index
            break

    if index == -1:
        return source_number

    shift_from_start = source_number - source_destination_map["source"][index]
    return source_destination_map["destination"][index] + shift_from_start


if __name__ == "__main__":
    main()
