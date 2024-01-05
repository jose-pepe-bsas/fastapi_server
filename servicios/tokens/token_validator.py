"""
Token validator module

While jwt (current token main library) holds its own data validation, 
this module will be used for project own token validation criteria.

As Example, we could get client_location_country from payload and deny service down.

For now is not implemented.
"""

class TokenValidator:
    def is_token_valid(self,token):
        return True


