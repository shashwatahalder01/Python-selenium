# import os
# from testconf.runconfiguration import stagingPortal, superAdmin
#
# class Data(object):
#     stagingPortal = stagingPortal
#     if stagingPortal:
#         # Staging portal
#         baseUrl = 'https://staging-admin.augmedix.com/'
#         if superAdmin:
#             username = 'admin-super@augmedix.com'
#             userPassword = 'Admin123$5557'
#         else:
#             username = 'admin_test@augmedix.com'
#             userPassword = 'Admin123$569'
#             adminName = 'Test Admins1'
#     else:
#         # Live portal
#         baseUrl = 'https://ee-admin.augmedix.com/'
#         if superAdmin:
#             username = 'admin-super@augmedix.com'
#             userPassword = 'Admin123$14'
#         else:
#             username = 'testops@augmedix.com'
#             userPassword = '@Admin13'
#
#     incorrectUserEmail = 'admin-super'
#     incorrectUsername = 'admin-@augmedix.com'  # correct email format
#     incorrectUserPassword = 'Admin'
#     newPassword = 'Admin123$4567'
#
#     # table
#     tableHeader = ['Name', 'Email', 'Type', 'Status', 'Settings']
#
#     classAttribute = 'class'
#     valueAttribute = 'value'
#     srcAttribute = 'src'
#     maxLengthAttribute = 'maxlength'
#
#     # attribute value
#     labelTextDisabled = 'text-disabled'
#     inputValue = 'false'
#     inputValue1 = 'DISALLOW_P2P'
#     featureValue = 'user-success'
#     emptyFeatureValue = ''
#     # emailClassError = 'user-error'
#     classError = 'user-error'
#     classSuccess = 'user-success'
#     classErrorSite = "errMsg"
#     classSuccessSite = 'successMsg'
#
#     # provider data
#     providerImagePath = os.path.abspath(os.getcwd()) + "\\data\\images\\user.jpg"
#     providerFourMBImagePath = os.path.abspath(os.getcwd()) + "\\data\\images\\4mbImage.jpg"
#     providerFirstname = 'Test'
#     providerLastname = 'Provider'
#     providerPhoneNumber = '(012) 345-6789'
#     providerInvalidPhoneNumber = 'Abcd@#$%!*'
#     providerEmptyPhone = '('
#     providerInvalidEmail = 'test_provider'
#     providerValidEmail = 'mandy_provider@augmedix.com'
#     testProviderId = 'TEST-TEST'
#
#     # Scribe data
#     scribeImagePath = os.path.abspath(os.getcwd()) + "\\data\\images\\user.jpg"
#     scribeFourMBImagePath = os.path.abspath(os.getcwd()) + "\\data\\images\\4mbImage.jpg"
#     scribeFirstname = 'Test'
#     scribeLastname = 'Scribe'
#     scribePhoneNumber = '(012) 345-6789'
#     scribeInvalidPhoneNumber = 'Abcd@#$%!*'
#     scribeEmptyPhone = '('
#     scribeInvalidEmail = 'test_scribe'
#     scribeValidEmail = 'test_scribe@augmedix.com'
#     testScribeId = '999999'
#     invalidScribeId = 'abcdef'
#     uniqueIdColumnName = 'Unique ID'
#     scribeDemoImageName = './common/images/demoavator.png'
#     scribeEmailInitialText = 'test_scribe_aug'
#     scribeEmailEndTextaug = '@augmedix.com'
#     scribeEmailEndText = '@advensus.com'
#     scribePasswordlimit = '8'
#     scribePartner = 'AXBD'
#     scribeProvider = 'Unassigned',
#     scribeEmailSubject = 'Augmedix SCRIBE Account Creation'
#
#
#     # log
#     deveiceLogs = 'Device Logs'
#     scribeLogs = 'Scribe Logs'
#
#     # alert message
#     largerImageAlert = 'File size is too large, maximum allowed file size is 3MB'
#     nonUniqueScribeIdAlert = 'Another scribe already has this Scribe ID. Scribe ID must be unique.'
#     siteCreateAlert = 'Failed to create Site!'
#     # success messsage
#     createScribeSuccessMessage = 'Scribe created Successfully'
#     emailSnippetsuperadmin = 'Hi Test Scribe, admin-super has created an account for you. Please click here to complete your registration. The link will expire in 24 hours.'
#     emailSnippetadmin = 'Hi Test Scribe, Test Admins1 has created an account for you. Please click here to complete your registration. The link will expire in 24 hours.'
#     siteCreateSuccessMessage = 'Site created Successfully'
#     # site
#     sitenamePrefix = 'Test_site_aug_'
#     siteName31 = 'abcdefghijklmnopqrstuvwxyzabcde'
#     siteNameMaxLength = '30'
#
#
#
#
