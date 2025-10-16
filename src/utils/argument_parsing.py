from argparse import ArgumentParser, Namespace

# function for getting arguments from cli
def parseLexerArgs() -> Namespace:
    parser = ArgumentParser()
    
    # I don't want to input my string, this flow is cleaner, like DUH
    parser.add_argument("--gramatics_file", dest="gramatics_file", type=str, help="file path for loading the grammar")
    parser.add_argument("--string", dest="string", type=str, help="the string that will be check on the grammar")



    parse_args = parser.parse_args()

    if parse_args.gramatics_file is None:
        raise Exception("Arguments where not suplly")

    return parse_args

