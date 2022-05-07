import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Subcat4Component } from './subcat4.component';

describe('Subcat4Component', () => {
  let component: Subcat4Component;
  let fixture: ComponentFixture<Subcat4Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Subcat4Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Subcat4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
