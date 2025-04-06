from claudette import Chat, models
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataGuy:
    """
    Main class for the DataGuy package.
    Handles interactions with Claude API for data science tasks.
    """
    
    def __init__(self, api_key=None, model=None):
        """
        Initialize the DataGuy object.
        
        Args:
            api_key (str, optional): Anthropic API key. If not provided, 
                                     will look for ANTHROPIC_API_KEY environment variable.
            model (str, optional): Claude model to use. Defaults to claude-3-5-sonnet.
        """
        self.api_key = api_key
        self.model = model or models[-1]  # Default to claude-3-5-sonnet
        self.chat = None
        self._initialize_chat()
        
    def _initialize_chat(self):
        """Initialize the Claude chat instance."""
        system_prompt = """You are DataGuy, an AI assistant specialized in data science.
        You help users analyze, visualize, and extract insights from data.
        When asked to perform data tasks, you will generate Python code that is correct,
        efficient, and follows best practices. The code should be ready to execute."""
        
        self.chat = Chat(self.model, sp=system_prompt)
    
    def wrangle(self, file_path):
        """
        Placeholder for the data wrangling function.
        Will be implemented in Phase 2.
        """
        pass
    
    def plot(self, data, description):
        """
        Placeholder for the plotting function.
        Will be implemented in Phase 2.
        """
        pass
    
    def analyze(self, data, description):
        """
        Placeholder for the analysis function.
        Will be implemented in Phase 2.
        """
        pass
