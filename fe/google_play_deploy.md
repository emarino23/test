
# Generate KeyStore
keytool -genkey -v -keystore android\app\beta.jks -keyalg RSA -keysize 2048 -validity 10000 -alias beta -storetype JKS

# Edit android\key.properties
password and info generated fron jks

# Generate Zip to Upload to Google Play
java -jar android\pepk.jar --keystore=android\app\beta.jks --alias=beta --output=output.zip --include-cert --encryptionkey=eb10fe8f7c7c9df715022017b00c6471f8ba81dasd49a11e6c09ffe3056a104a3bbe4ac5a955f4ba4fe93fc8cef275asdasd9d2a529a2092761fb833b656cd48b9de6a

# Change Version to Android on pubspec.yaml
version: 0.0.1+000003
# Generate App Bundle to upload to Google Play
flutter build appbundle --no-sound-null-safety    