package com.example.place4u

import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.GeolocationPermissions
import android.webkit.WebChromeClient
import android.webkit.WebView
import android.webkit.WebViewClient
import android.Manifest
import android.annotation.SuppressLint
import android.app.Activity
import android.content.DialogInterface
import android.content.Intent
import android.content.IntentSender
import android.location.Location
import android.net.Uri
import android.os.Build
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.core.content.ContextCompat
import com.google.android.gms.common.api.ResolvableApiException
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationCallback
import com.google.android.gms.location.LocationRequest
import com.google.android.gms.location.LocationServices
import com.google.android.gms.location.LocationSettingsRequest
import com.google.android.gms.location.LocationSettingsResponse
import com.google.android.gms.location.SettingsClient
import com.google.android.gms.tasks.OnFailureListener
import com.google.android.gms.tasks.OnSuccessListener
class MainActivity : AppCompatActivity() {
    private val REQUEST_PERMISSIONS_REQUEST_CODE = 1981
    private val REQUEST_CODE_LOCATION_SETTINGS = 2981
    private val PERMISSIONS = arrayOf(
        Manifest.permission.ACCESS_FINE_LOCATION,
        Manifest.permission.ACCESS_COARSE_LOCATION
    )
    private var mFusedLocationClient: FusedLocationProviderClient? = null
    private var mSettingsClient: SettingsClient? = null
    private var mLocationRequest: LocationRequest? = null
    private var mLocationCallback: LocationCallback? = null
    private var mLocationSettingsRequest: LocationSettingsRequest? = null
    private var mLastLocation: Location? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (checkSelfPermission(android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION), 1)
        }
        val myWebView: WebView = findViewById<WebView>(R.id.myWebView)
        myWebView.settings.run {
            // 웹뷰 자바스크립트 허용
            javaScriptEnabled = true
            javaScriptCanOpenWindowsAutomatically = true
            setSupportMultipleWindows(true)
        }

        myWebView.webViewClient = WebViewClient()
        myWebView.webChromeClient = WebChromeClient()
        myWebView.webChromeClient = object : WebChromeClient(){
            override fun onGeolocationPermissionsShowPrompt(
                origin: String?,
                callback: GeolocationPermissions.Callback?
            ) {
                super.onGeolocationPermissionsShowPrompt(origin, callback)
                callback?.invoke(origin,true,false)
            }
        }
        myWebView.loadUrl("https://place4u.kro.kr")
        init()

        //checkLocation()


    }
    override fun onBackPressed() { // 뒤로가기 기능 구현

        val myWebView: WebView = findViewById<WebView>(R.id.myWebView)
        if(myWebView.canGoBack()){
            myWebView.goBack()
        }else{

            finish()
        }
        super.onBackPressed()
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_CODE_LOCATION_SETTINGS) {
            when (resultCode) {
                Activity.RESULT_OK -> Toast.makeText(this, "Result OK", Toast.LENGTH_SHORT).show()
                Activity.RESULT_CANCELED -> Toast.makeText(this, "Result Cancel", Toast.LENGTH_SHORT).show()
            }
        }
    }
    private fun init() {
        if (mFusedLocationClient == null) {
            mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
        }

        mSettingsClient = LocationServices.getSettingsClient(this)

        mLocationRequest = LocationRequest().apply {
            interval = 20 * 1000
            priority = LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY
        }

        val builder = LocationSettingsRequest.Builder()
        builder.addLocationRequest(mLocationRequest!!)
        mLocationSettingsRequest = builder.build()
        checkLocation()
    }
    private fun checkLocation() {
        if (isPermissionGranted()) {
            startLocationUpdates()
        } else {
            requestPermissions()
        }
    }

    private fun isPermissionGranted(): Boolean {
        for (permission in PERMISSIONS) {
            if (permission == Manifest.permission.ACCESS_BACKGROUND_LOCATION && Build.VERSION.SDK_INT < Build.VERSION_CODES.Q) {
                continue
            }
            val result = ContextCompat.checkSelfPermission(this, permission)
            if (PackageManager.PERMISSION_GRANTED != result) {
                return false
            }
        }
        return true
    }

    private fun requestPermissions() {
        requestPermissions(PERMISSIONS, REQUEST_PERMISSIONS_REQUEST_CODE)
    }

    private fun startLocationUpdates() {
        mSettingsClient?.checkLocationSettings(mLocationSettingsRequest!!)?.addOnSuccessListener(this, OnSuccessListener<LocationSettingsResponse> {
            // onSuccess
        })?.addOnFailureListener(this, OnFailureListener { e ->
            if (e is ResolvableApiException) {
                resolveLocationSettings(e)
            } else {
                // Handle other errors
            }
        })
    }

    private fun resolveLocationSettings(exception: Exception) {
        val resolvable = exception as ResolvableApiException
        try {
            resolvable.startResolutionForResult(this, REQUEST_CODE_LOCATION_SETTINGS)
        } catch (e1: IntentSender.SendIntentException) {
            e1.printStackTrace()
        }
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == REQUEST_PERMISSIONS_REQUEST_CODE) {
            when {
                grantResults.isEmpty() -> {
                    // If user interaction was interrupted, the permission request is cancelled
                    // and you receive empty arrays.
                }
                grantResults[0] == PackageManager.PERMISSION_GRANTED -> {
                    // Permission granted.
                    startLocationUpdates()
                }
                else -> {
                    // Permission denied.
                    for (permission in permissions) {
                        if ("android.permission.ACCESS_FINE_LOCATION" == permission) {
                            val builder = AlertDialog.Builder(this)
                            builder.setTitle("알림")
                            builder.setMessage("위치 정보 권한이 필요합니다.\n\n[설정]->[권한]에서 '위치' 항목을 사용으로 설정해 주세요.")
                            builder.setPositiveButton("OK") { _, _ ->
                                val intent = Intent()
                                intent.action = android.provider.Settings.ACTION_APPLICATION_DETAILS_SETTINGS
                                intent.data = Uri.fromParts("package", packageName, null)
                                startActivity(intent)
                            }
                            builder.setNegativeButton("Cancel") { _, _ ->
                                Toast.makeText(this, "Cancel Click", Toast.LENGTH_SHORT).show()
                            }
                            val alertDialog: AlertDialog = builder.create()
                            alertDialog.show()
                        }
                    }
                }
            }
        }
    }
}