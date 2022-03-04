from brownie import project
'''
    we load the superfluid project interfaces using brownie
    this allows us to interact with the contracts' interfaces
'''

'''
    @dev: we load the project as superfluid.
    @dev: this gives a project object with all the interfaces and contracts if available
'''
superfluid = project.load("./superfluid-py")

'''
    we load the project's configuration
'''
superfluid.load_config()

