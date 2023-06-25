# Sports Betting Arbitrage Detector

This project involves scraping data from sports betting companies (Novibet, Stoiximan), processing the data, and then finding arbitrage opportunities between the two companies. The main technologies used include Python for web scraping and data processing, and SQL for querying and identifying arbitrage opportunities.



## Project Structure

1. **Web_scrape_functions.** Contains `novibet_functions.py` and `stoiximan_functions.py`  The scripts uses Selenium to navigate the Novibet/Stoiximan website and extract football/basketball/tennis betting data. The extracted data is then processed and written to a CSV file.

2. **Web_scrape_functions_deb.** The same scripts as above used in ipynb format for debugging in scapping and data collection process

3. **Main_scripts.** Contains the `main.ipynb` that call the above functions performs the matching of the games and arbitrage calculations. Then, `queries.py` process the betting data and identify arbitrage opportunities. The script includes two queries, one for over/under bets and one for goal-goal/no goal bets.

## How to Use

1. Run the `main_scipts/main.ipynb`. If the scrape scripts doesn't return results, they need modification to be up to date.


## Contributing
Contributions are welcomed! To contribute:

1. Fork the project
2. Create your feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/YourFeature)
5. Open a pull request


## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.