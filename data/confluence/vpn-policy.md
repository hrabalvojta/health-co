# VPN Policy — EuroHealth Insurance AG

## Overview
All remote employees must use the company VPN to access internal resources. This policy applies to all 8 EU office locations.

## Setup Instructions

### Windows
1. Open Settings → Network & Internet → VPN
2. Click "Add a VPN connection"
3. Server: `vpn.eurohealth.internal`
4. Use your Active Directory credentials (same as email login)
5. Connection type: IKEv2

### macOS
1. System Settings → Network → VPN
2. Click "+" to add new VPN
3. Type: IKEv2
4. Server: `vpn.eurohealth.internal`
5. Remote ID: `vpn.eurohealth.internal`

## Password Reset
If your VPN password is not working:
1. Go to https://password.eurohealth.internal
2. Click "Reset VPN Password"
3. Authenticate with your email and 2FA code
4. New password will be active within 5 minutes

## Troubleshooting
- **Connection drops frequently**: Check your internet stability. Try switching between Wi-Fi and wired connection.
- **"Authentication failed" error**: Ensure Caps Lock is off. Try resetting password (see above).
- **Cannot reach internal sites after connecting**: Contact IT Support at it-support@eurohealth.eu.

## Policy
- VPN must be active for ALL access to internal systems when outside office network
- Split tunneling is DISABLED for security compliance
- Sessions timeout after 8 hours of inactivity
- Maximum 2 concurrent VPN sessions per user
