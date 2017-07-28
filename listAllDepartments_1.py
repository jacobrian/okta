'''
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
'''
#For more information on requests and how to download, visit:
#	http://docs.python-requests.org/en/latest/user/quickstart/
import requests
import json

def listUsersRestCall(url,headers):
	theRequest = requests.get(url, headers=headers)
	dataToReturn = []
	
	if theRequest.status_code == requests.codes.ok:
		response = json.loads(theRequest.text)
		for user in response:
 			dataToReturn.append( user["profile"].get("department"))
		departmentset = set(dataToReturn)
		if 'next' in theRequest.links:
			return departmentset.union(listUsersRestCall(theRequest.links["next"]["url"],headers))
		else:
			return departmentset
	else:
		raise Exception(theRequest.text)

org = "https://okta.okta.com"
apiToken = "yeah right buddy..." 

baseUrl= org+ "/api/v1/"
headers= {"Accept":"application/json","Content-Type":"application/json","Authorization":"SSWS "+apiToken}
getUsersUrl = "users"

#Get the users and print the number of users
listcostcenters = listUsersRestCall(baseUrl+getUsersUrl,headers)
deptsorted = sorted(listcostcenters)
for depts in deptsorted:
	print depts
