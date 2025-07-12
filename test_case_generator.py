import json
import random
import argparse
import uuid

def generate_streamer_id():
    return str(uuid.uuid4())

def generate_section(section_id, num_streams, dup_prob):
    ids = [generate_streamer_id() for _ in range(max(3, int(num_streams/2)))]
    section_data = []
    for _ in range(num_streams):
        if random.random() < dup_prob and section_data:
            # Duplicate a previous ID
            sid = random.choice(section_data)['streamerID']
        else:
            sid = random.choice(ids)
        section_data.append({'streamerID': sid})
    return {
        'sectionID': section_id,
        'sectionData': section_data
    }

def main():
    parser = argparse.ArgumentParser(description='Generate random test input for StreamFix Pro.')
    parser.add_argument('-s', '--sections', type=int, default=3, help='Number of sections')
    parser.add_argument('-n', '--streams', type=int, default=20, help='Streams per section')
    parser.add_argument('-d', '--dup-prob', type=float, default=0.3, help='Probability of duplicate in top N')
    parser.add_argument('-o', '--output', default='input.json', help='Output file name')
    args = parser.parse_args()

    data = []
    for i in range(args.sections):
        section_id = f'Section_{i+1}'
        section = generate_section(section_id, args.streams, args.dup_prob)
        data.append(section)
    with open(args.output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {args.sections} sections with {args.streams} streams each (dup prob {args.dup_prob}) in {args.output}")

if __name__ == '__main__':
    main() 