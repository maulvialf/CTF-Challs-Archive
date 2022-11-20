@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Dashboard') }}</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    <p>Dapatkan sebuah flag setelah mengundang 15 orang!</p>
                    <p>Flag dapat ditukarkan menjadi dollar... <i>tapi boong :P</i></p>
                    <br>
                    <strong><p>Referer: {{$referer}}</p></strong>
                    <strong><p>Flag: <i>{{$flag}}</i></p></strong>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
