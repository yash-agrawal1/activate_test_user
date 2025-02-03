import yaml

def parse_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        domain = config.get('domain')
        chunk_size = config.get('chunk_size')
        return domain, chunk_size

if __name__ == "__main__":
    domain, chunk_size = parse_config('config.yaml')
    print(f"Domain: {domain}")
    print(f"Chunk Size: {chunk_size}")
